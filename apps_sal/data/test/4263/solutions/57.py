text = input()

count = 0
max_count = 0
for i in range(len(text)):
    if text[i] == "A" or text[i] == "C" or text[i] == "G" or text[i] == "T":
        count += 1
    else:
        if max_count < count:
            max_count = count
            count = 0
        else:
            count = 0

print(max(max_count, count))
