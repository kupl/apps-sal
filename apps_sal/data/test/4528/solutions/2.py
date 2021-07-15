q = int(input())
for z in range(q):
     a, b = map(int, input().split())
     s = (23 - a) * 60 + (60 - b)
     print(s)
