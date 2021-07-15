n = int(input())
aa = list(map(int, input().split()))

for a in aa:
  if a % 2 == 0 and a % 3 != 0 and a % 5 != 0:
    print('DENIED')
    return
print('APPROVED')
