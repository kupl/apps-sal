n = int(input())
s = list(input())
count=0
for i in range(n-2):
    if s[i] == "A":
        if s[i+1] == "B":
            if s[i+2] == "C":
                count+=1
print(count)
