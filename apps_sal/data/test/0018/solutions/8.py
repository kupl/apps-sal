import sys
import collections

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        del self.stack[len(self.stack)-1]

    def top(self):
        return self.stack[len(self.stack)-1]

    def empty(self):
        return len(self.stack) == 0

def main():
    s = list(sys.stdin.readline().split()[0])

    hist = [0 for i in range(256)]

    for c in s:
        hist[ord(c)]+=1

    cur = 0
    u = []
    t = []

    minn = ord('a')
    for i in range(minn, ord('z')+1):
        if(hist[i]):
            minn = i
            break
    aux = []
    while cur < len(s):
        aux.append(s[cur])
        hist[ord(s[cur])] -= 1

        if(s[cur] == chr(minn)):
            u += aux
            aux = []
            minn = ord('z')
            for i in range(ord('a'), ord('z')+1):
                if(hist[i]):
                    minn = i
                    break

            while(len(u) and ord(u[-1]) <= minn):
                t.append(u[-1])
                del u[-1]
        cur += 1


    print("".join(t))

main()

