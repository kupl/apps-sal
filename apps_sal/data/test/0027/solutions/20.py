n = int(input())
seq = input()
count = n
for i in range(1,n//2+1):
    if seq[0:i] == seq[i:min(2*i,n)]:
        count = n + 1 - i
print(count)
