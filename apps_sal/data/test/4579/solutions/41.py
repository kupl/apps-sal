n = int(input())
keihin = {}
for i in range(n):
    moji = str(input())
    keihin.setdefault(moji,0)
    keihin[moji]+=1
print(len(keihin.keys()))
