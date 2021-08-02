N = int(input())
S = list(input())

counter = 0
li = [0]
for i in range(N):
    if S[i] == 'I':
        counter += 1
    else:
        counter -= 1
    li.append(counter)
print(max(li))
