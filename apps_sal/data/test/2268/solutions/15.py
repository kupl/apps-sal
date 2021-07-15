#In the name of Allah

from sys import stdin, stdout
input = stdin.readline
d = {'x': 'x', 'y': 'y', 'z': 'z', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u', 'v': 'v', 'w': 'w', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g'}
n, m = list(map(int, input().split()))

s = input()

xy = [input()for i in range(m)]

for i in d:
        t = i
        for j in xy:
                if j[0] == t:
                        t = j[2]
                elif j[2] == t:
                        t = j[0]
        d[i] = t
                        
        
for i in range(n):
        stdout.write(d[s[i]])


