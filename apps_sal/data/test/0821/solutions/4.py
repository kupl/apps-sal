s, v1, v2, t1, t2 = map(int,input().split())
res1 = 2*t1+s*v1
res2 = 2*t2+s*v2
if res1 == res2: print("Friendship")
elif res1 < res2: print("First")
else: print("Second")
