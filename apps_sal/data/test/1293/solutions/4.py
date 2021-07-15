n = int(input())
b = list(map(int, input().split()))
moves = 0
sum = 0
for i in range(n):
    moves += abs(b[i] + sum)
    sum -= (b[i] + sum)
print(moves)    
