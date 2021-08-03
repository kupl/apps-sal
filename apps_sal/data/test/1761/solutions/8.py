n = int(input())
ref = '<3'
words = []

for i in range(n):
    words.append(input())

ref = ref + '<3'.join(words) + ref

message = input()
i, j = 0, 0
while i < len(ref) and j < len(message):
    if ref[i] == message[j]:
        i += 1
    j += 1

if i == len(ref):
    print("yes")
else:
    print("no")
