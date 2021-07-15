# cook your dish here
word = input().strip()

max_val = 0
for i in range(len(word)-1):
    for j in range(i+1,len(word)):
        if(word[i]!=word[j] and abs(i-j)>max_val):
            max_val = abs(i-j)
print(max_val)
