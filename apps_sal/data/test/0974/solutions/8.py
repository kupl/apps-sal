n = int(input())
indexToDel = 1
stack = [];
count = 0;
for i in range(n*2):
    line = input().split()
    if line[0] == 'remove':
        if len(stack) != 0:
            if stack[-1] == indexToDel:
                stack.pop();
            else:
                count+=1
                stack = []
        indexToDel+=1
    else:
        stack.append(int(line[1]))
        
print(count)
