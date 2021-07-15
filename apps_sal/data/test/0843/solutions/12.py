n = int(input())
s = input()
a = list(map(int, input().split()))
WAS = False
pos = 1
for i in range(0, n) :
    if s[pos - 1] == '<' : pos -= a[pos - 1]
    else : pos += a[pos - 1]
    if pos < 1 or pos > n : WAS = True
    if WAS : break
if WAS : print("FINITE")
else : print("INFINITE")


