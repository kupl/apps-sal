class mystr:
    def __init__(self, string):
        self.value = string

    def isEven(self):
        l = len(self.value)
        if (not l & 1) and self.value[:l // 2] == self.value[l // 2:]:
            return True
        else:
            return False

    def pop(self):
        l = len(self.value)
        self.value = self.value[:l - 1]


s = mystr(input())
l = len(s.value)
for i in reversed(list(range(l))):
    s.pop()
    if s.isEven():
        print(i)
        break
