q = int(input())
for _ in range(q):
    o1, o2, t1, t2 = map(int,input().split())
    answer = True
    if t2 > min(o1,o2):
        answer = False
    if t1 + t2 > o1 + o2:
        answer = False
    if answer:
        print("Yes")
    else:
        print("No")
