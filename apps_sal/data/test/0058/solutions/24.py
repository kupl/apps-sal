bar = int(input())
side = int(input())
top = int(input())


current_bar = bar
num_bars = 1
dim = [side] * 4 + [top] * 2
dim.sort()
while dim != []:
    #print (current_bar)
    if current_bar < min(dim):
        current_bar = bar
        num_bars += 1
    
    if current_bar >= dim[-1]:
        current_bar -= dim.pop()
        
    if dim != [] and current_bar >= dim[0]:
        current_bar -= dim.pop(0)

print (num_bars)

