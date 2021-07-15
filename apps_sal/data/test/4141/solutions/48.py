n = int(input())
l1 = list(map(int,input().split()))
l2 = []
cnt = 0

for i in l1 :
    if i%2 == 0 :
        l2.append(i)
        cnt += 1

for i in l2 :
    if i%3 != 0 and i%5 != 0 :
        print('DENIED')
        return

print('APPROVED')
