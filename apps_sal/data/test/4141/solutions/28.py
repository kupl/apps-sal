n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    no = a[i]
    if (no%2==0) and (no%3!=0) and (no%5!=0):
        print('DENIED')
        return
print('APPROVED')
