A, B, C = map(int,input().split())

count = 0

if A == B:
    count += 1
if B == C:
    count += 1
if A == C:
    count += 1

if count == 1:
    print('Yes')
else:
    print('No')
