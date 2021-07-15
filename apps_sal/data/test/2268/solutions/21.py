import string
n, m = input().split()
n, m = [int(n), int(m)]
name = input()
name = list(name)
buffer = {}
for ch in list(string.ascii_lowercase):
  buffer[ch] = [] 
for i in range(n):
  buffer[name[i]].append(i)
for j in range(m):
  xi, yi = input().split()
  temp = buffer[xi]
  buffer[xi] = buffer[yi]
  buffer[yi] = temp
for key, value in list(buffer.items()):
  for i in value:
    name[i] = key
name = "".join(name)
print(name)

