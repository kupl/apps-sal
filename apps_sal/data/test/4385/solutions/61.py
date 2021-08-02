s = []
for i in range(5):
    s.append(int(input()))
k = int(input())
for i in range(4):
    if s[i + 1] - s[0] > k:
        print(":(")
        break
else:
    print("Yay!")
