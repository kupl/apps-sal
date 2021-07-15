n=int(input())//2
s=input()
print("YNeos"[s[:n]!=s[n:]::2])
