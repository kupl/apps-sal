def f(word):
    return len(list([x for x in word if x.isupper()]))


_ = input()
s = input().split()
print(max(f(word) for word in s))
