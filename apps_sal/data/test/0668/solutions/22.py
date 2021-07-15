def multiple_max(lst, count):
    result = []

    for k in range(count):
        max = -1
        max_i = 0
        for i in range(len(lst)):
            if i not in result and not is_notified[i]:
                if lst[i] > max:
                    max = lst[i]
                    max_i = i
        if max != -1:
            result.append(max_i)

    return result


n = input()
message_counts = [int(x) for x in input().split(" ")]
is_notified = [False for x in range(len(message_counts))]
is_notified[0] = True
chat = []


def say(idx):
    indices_to_say = multiple_max(message_counts, message_counts[idx])
    if len(indices_to_say) is 0:
        return

    for idx_to_notify in indices_to_say:
        is_notified[idx_to_notify] = True

    for next_idx in indices_to_say:
        message_counts[idx] -= 1
        chat.append(str(idx + 1) + " " + str(next_idx + 1))
        say(next_idx)


say(0)

result = True
for x in is_notified:
    if not x:
        result = False
        break

if result:
    print(len(chat))
    for message in chat:
        print(message)
else:
    print(-1)
