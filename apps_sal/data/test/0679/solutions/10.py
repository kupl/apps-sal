s = input()
for i in range(len(s) - 2):
    if sorted(s[i:i + 3]) == ['A', 'B', 'C']:
        print("Yes")
        break
else:
    print("No")
