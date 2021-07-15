import sys

a1,b1 = map(int, input().split())
a2,b2 = map(int, input().split())
a, b = a1 * b1, a2 * b2
cnta2, cntb2, cnta3, cntb3 = 0, 0, 0, 0
ans = 0
while a%2==0:
	a //= 2
	cnta2 += 1
while a%3==0:
	a //= 3
	cnta3 += 1

while b%2==0:
	b //= 2
	cntb2 += 1
while b%3==0:
	b //= 3
	cntb3 += 1

if a != b:
	print(-1)
	return

dif = cnta3 - cntb3
if dif > 0:
  for i in range(dif):
     ans += 1
     if a1 % 3 == 0:
     	a1 = a1 * 2 // 3
     else:
     	b1 = b1 * 2 // 3
else:
  for i in range(-dif):
     ans += 1 
     if a2 % 3 == 0:
     	a2 = a2 * 2 // 3
     else:
     	b2 = b2 * 2 // 3

a, b = a1 * b1, a2 * b2

cnta, cntb = 0, 0

while a % 2 == 0:
  a = a // 2
  cnta += 1

while b % 2 == 0:
  b = b // 2
  cntb += 1

dif = cnta - cntb
if dif > 0:
  for i in range(dif):
     ans += 1
     if a1 % 2 == 0:
     	a1 = a1 // 2
     else:
     	b1 = b1 // 2
else:
  for i in range(-dif):
     ans += 1
     if a2 % 2 == 0:
     	a2 = a2 // 2
     else:
     	b2 = b2 // 2

print(ans)
print(str(a1) + ' ' + str(b1))
print(str(a2) + ' ' + str(b2))
