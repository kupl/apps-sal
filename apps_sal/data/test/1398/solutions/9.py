import bisect
def physics(f):
        num = int(file.readline())
        res = list(map(int,file.readline().split()))
        res.sort()
        y = res[num-1]
        x = res[0]
        m = num
        if y <= 2*x:
               return 0
        else:
          for index,x in enumerate(res):
             y = 2*x
             i = bisect.bisect(res,y,index+1,num)
             
             if res[i-1] <= 2*x:   
                     removes = (index + num - i)
                     m = min(m,removes)
             if index >= m:
                    return m
        

file = open('input.txt', 'r')
open('output.txt', 'w').write(str(physics(file)))

