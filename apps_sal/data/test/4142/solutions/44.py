s = [c for c in input()]
result = 'Yes'
for index, step in enumerate(s, start=1):
    if index % 2 == 1:
        if step not in "RUD":
            result = 'No'
            break
    else:
        if step not in "LUD":
            result = 'No'
            break

print(result)
