n = int(input())
s = input()
s1 = set([s[i: j] for i in range(len(s))
          for j in range(i + 1, len(s) + 1)])

for val in sorted(s1, key=len, reverse=True):
    if(val == val[::-1]):
        print(len(val))
        print(val)
        break
