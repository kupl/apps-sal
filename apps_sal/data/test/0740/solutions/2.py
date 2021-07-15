class step(object):
    timer = []
    def __init__(self, name, machin_num, step_time):
        self.machin_num = machin_num
        self.step_time = step_time
        self.name = name

    def step_input(self, cloth_num, t):
        '''
        if cloth_num + len(self.timer) > self.machin_num:
            excloth = cloth_num + len(self.timer) - self.machin_num
            print('%s error excloth is %d' %(self.name , excloth))
            return 'error'
        else:
            for new_cloth in range(cloth_num):
                self.timer.append(t)
            #print(self.timer)
        '''
        for new_cloth in range(cloth_num):
                self.timer.append(t)

    def step_run(self, t):
        tmptimer = [each_timer for each_timer in self.timer if t - each_timer < self.step_time]
        #next_num = len(self.timer) - len(tmptimer)
        self.timer = tmptimer
        #if len(self.timer) == 0:
            #print('%s in %d is empty' %(self.name, t))
            #pass
        #print('%d: %s timer:\n%s \n' %(t, self.name, self.timer))
        #print('%d: %s timer: %d \n' %(t, self.name, next_num))
        #return next_num
            
    def checkstate(self, pre_t):
        running_machine = len(self.timer)
        #output = 0
        for each_timer in range(running_machine):
            if pre_t - self.timer[each_timer] >= self.step_time:
                running_machine -= 1
                #output += 1
        return self.machin_num - running_machine
        

def main():
    p, n1, n2, n3, t1, t2, t3 = list(map(int, input().split()))
    '''
    p = 8
    n1 = 4
    n2 = 3
    n3 = 2
    t1 = 10
    t2 = 5
    t3 = 2
    '''
    step1 = step('step1', n1, t1)
    step2 = step('step2', n2, t2)
    step3 = step('step3', n3, t3)

    t = 0
    #cp = 0
    while True:
        pre_num1 = step1.checkstate(t)
        pre_num2 = step2.checkstate(t + t1)
        pre_num3 = step3.checkstate(t + t1 + t2)        
        step1_input = min(pre_num1, pre_num2, pre_num3)
        p -= step1_input
        step1.step_run(t)
        step1.step_input(step1_input, t)
        step2.step_run(t + t1)
        step2.step_input(step1_input, t + t1)
        step3.step_run(t + t1 + t2)
        step3.step_input(step1_input, t + t1 + t2)
        if p <= 0:
            print(t + t1 + t2 + t3)
            break
        pre_t = []
        if len(step1.timer) == step1.machin_num:
            #print('step1 stun')
            pre_t.append(t1 - (t - step1.timer[0]))
        if len(step2.timer) == step2.machin_num:
            #print('step2 stun')
            pre_t.append(t2 - (t + t1 - step2.timer[0]))
        if len(step3.timer) == step3.machin_num:
            #print('step3 stun')
            pre_t.append(t3 - (t + t1 + t2 - step3.timer[0]))
        #print('pre_t: %s' %(pre_t))
        if len(pre_t) == 0:
            pre_t = 1
        else:
            pre_t = min(pre_t)
        '''
        print('%d  minute input: %d' %(t, step1_input))
        print('step1 timer:\n%s\npre_num1: %d'%(step1.timer, pre_num1))
        print('step2 timer:\n%s\npre_num2: %d'%(step2.timer, pre_num2))
        print('step3 timer:\n%s\npre_num3: %d'%(step3.timer, pre_num3))
        print('pre_t:  %d' %pre_t)
        
        input()
        '''
        t += pre_t

def __starting_point():  
    main()

__starting_point()
