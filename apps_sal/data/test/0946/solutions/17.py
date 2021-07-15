n = int(input())
s = [int(x) for x in input().split()]
for i in range(n):
    if (s[i] == 1):
        print("HARD")
        quit()
print("EASY")

