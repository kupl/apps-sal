s=(input())[::-1]
T=["dream", "dreamer", "erase","eraser"]
T=[x[::-1] for x in T]
cur=""
for e in s:
    cur+=e
    if(cur in T):
        cur=""
print(("YES" if cur=="" else "NO"))

