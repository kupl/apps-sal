n = int(input())
a = list(map(int,input().split()))
left = [None for _ in range(n)]
right = [None for _ in range(n)]
left1 = [None for _ in range(n)]
right1 = [None for _ in range(n)]
class Stack(object):
    def __init__(self):
        self.c = []
    def push(self,new):
        self.c.append(new)
    def pop(self):
        return self.c.pop(-1)
    def vide(self):
        return self.c == []
    def peek(self):
        return self.c[-1]
def calculleft():
    s = Stack()
    for i in range(n):
        while not s.vide() and a[s.peek()] > a[i]:
            s.pop()
        if not s.vide():
            left[i] = s.peek()
        else:
            left[i] = -1
        s.push(i)

def calculright():
    s = Stack()
    for i in range(n-1,-1,-1):
        while not s.vide() and a[s.peek()] >= a[i]:
            s.pop()
        if not s.vide():
            right[i] = s.peek()
        else:
            right[i] = n
        s.push(i)
        
def calculleft1():
    s = Stack()
    for i in range(n):
        while not s.vide() and a[s.peek()] < a[i]:
            s.pop()
        if not s.vide():
            left1[i] = s.peek()
        else:
            left1[i] = -1
        s.push(i)

def calculright1():
    s = Stack()
    for i in range(n-1,-1,-1):
        while not s.vide() and a[s.peek()] <= a[i]:
            s.pop()
        if not s.vide():
            right1[i] = s.peek()
        else:
            right1[i] = n
        s.push(i)
     
res = 0
calculleft()
calculright()
calculleft1()
calculright1()

res2 = 0
for i in range(n):
    res += (i-left[i])*(right[i]-i)*a[i]
    res2 += (i-left1[i])*(right1[i]-i)*a[i]
print(res2-res)
    

