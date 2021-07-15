N = int(input())

answer = 0

for i in range(1,N + 1):
     if len(str(i)) % 2 == 1:
        answer += 1

print(answer)
