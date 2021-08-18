# TL

data = input().split(" ")
n = int(data[0])
m = int(data[1])
correct = input().split(" ")
correct = [int(x) for x in correct]
wrong = input().split(" ")
wrong = [int(x) for x in wrong]
limit = max(max(correct), min(correct) * 2)
for i in range(len(wrong)):
    if wrong[i] <= limit:
        print("-1")
        return
for i in range(len(correct)):
    if correct[i] > limit:
        print("-1")
        return
print(limit)
