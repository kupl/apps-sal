string = input()
difference = []
for i in range(0, len(string) - 2):
    difference.append(abs(int(string[i:i + 3]) - 753))
print(min(difference))
