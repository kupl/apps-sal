n = int(input())

a = input()
a = list(map(int, a.split(' ')))
user_index = []
recived = []
for i in range(n):
    user_index.append(i)
    recived.append(0)
recived[0] = 1
count = 0
answer = ''

k = 1
while k < len(a):
    for i in range(1, n - k):
        if a[i] < a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            user_index[i], user_index[i + 1] = user_index[i + 1], user_index[i]
    k += 1

if a[0] != 0:
    for i in range(n):
        user = 0
        while(a[i] > 0 and sum(recived) != n):
            user += 1
            if(user < n and recived[user_index[user]] != 1):
                recived[user_index[user]] = 1
                count += 1
                answer += str(user_index[i] + 1) + ' ' + str(user_index[user] + 1) + '\n'
                a[i] -= 1
    if sum(recived) == n:
        print(count)
        print(answer)
    else:
        print(-1)
else:
    print(-1)
