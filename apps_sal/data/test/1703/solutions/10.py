class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


def check(str):
    st = Stack()
    for i in str:
        if i == "(":
            st.push(i)
        else:
            if not st.isEmpty():
                if st.peek() == "(":
                    st.pop()
                else:
                    st.push(i)
            else:
                st.push(i)
    return st.items


def count_it(str):
    opens = 0
    closes = 0
    for i in str:
        if i == "(":
            opens += 1
        else:
            closes += 1
    return (opens, closes)


n = int(input())
strings = []
for i in range(n):
    strings.append(input())

results = []

for i in strings:
    results.append(check(i))

maybe = []
for i in results:
    o, c = count_it(i)
    if o == 0 or c == 0:
        maybe.append((o, c))

ht = {}
for i in maybe:
    if ht.get(i, None) == None:
        ht[i] = 1
    else:
        ht[i] += 1

ans = 0
for o, c in maybe:
    if c == 0 and o != 0:
        if ht.get((c, o), None) != None:
            ans += ht[(c, o)]
    elif o == 0 and c == 0:
        ans += ht[(0, 0)]

print(ans)
