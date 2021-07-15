n = int(input())
moves = input()
i = n
count = 0
while(i < len(moves)):
    m = moves[i - 1] 
    if(m == moves[i - 2] and m == moves[i - 3] and m == moves[i - 3]):
        count += 1
    i += n
print(count)
