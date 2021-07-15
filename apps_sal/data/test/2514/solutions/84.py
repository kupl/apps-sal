from collections import Counter
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
su = sum(A)
counter = Counter(A)
lis = {}
for i in range(Q):
  B, C = map(int, input().split())
  su -= B * counter[B]
  su += C * counter[B]
  counter[C] += counter[B]
  counter[B] = 0
  print(su)
