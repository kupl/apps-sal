input_data = input()
counts = []
count = 0

for i in range(3):
  if input_data[i] == "R":
    count += 1
  else:
    counts.append(count)
    count = 0

counts.append(count)

counti = max(counts)
print(counti)
