N, K=map(int, input().split())
count=0
while True:
    if N >= pow(K, count):
        count+=1
    else:break
print(count)
