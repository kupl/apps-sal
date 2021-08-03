from collections import deque

s = {}

s = {
    "a": deque(list(input())),
    "b": deque(list(input())),
    "c": deque(list(input())),
}

t = "a"

while s[t]:
    t = s[t].popleft()

print((t.upper()))
