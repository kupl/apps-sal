n = int(input())
prev = []
this = []
for i in range(n):
    prev.append(input())
for i in range(n):
    this.append(input())
for i in range(n):
    if prev[i] in this:
        this.remove(prev[i])
print(len(this))
