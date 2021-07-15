n,k = map(int,input().split())
l = list(map(int, input().split()))
freq = [0]*(n+1)
for i in l:
    freq[i]+=1
freq.sort()
vf = len(freq) - k if len(freq)> k else 0
print(sum(freq[:vf]))
