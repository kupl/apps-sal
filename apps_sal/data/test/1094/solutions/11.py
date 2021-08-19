order = []
users_set = set()
count = int(input())
messages = []
for _ in range(count):
    messages.append(input())
for user in reversed(messages):
    if user not in users_set:
        order.append(user)
        users_set.add(user)
print('\n'.join(order))
