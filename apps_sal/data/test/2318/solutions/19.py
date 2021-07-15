import sys


input = sys.stdin.readline
n = int(input())
word = [input() for i in range(2*n)]

for i in range(n):
    word0 = word[i*2]
    word1 = word[i*2 + 1]
    li0 = [[word0[0], 1]]
    li1 = [[word1[0], 1]]
    for i in range(1, len(word0)):
        if li0[-1][0] == word0[i]:
            li0[-1][1] += 1
        else:
            li0.append([word0[i], 1])

    for i in range(1, len(word1)):
        if li1[-1][0] == word1[i]:
            li1[-1][1] += 1
        else:
            li1.append([word1[i], 1])
    for i in range(len(li0)):
        if li0[i][0] == li1[i][0] and li0[i][1] <= li1[i][1]:
            continue
        else:
            print("NO")
            break
    else:
        print("YES")
          


