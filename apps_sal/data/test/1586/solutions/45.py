N = int(input())
if N % 2 == 1:
    Answer = 0
else:
    Answer = 0
    for i in range(1, 100):
        Answer += N // (2 * 5 ** i)
print(Answer)
