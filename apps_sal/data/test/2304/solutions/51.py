from collections import namedtuple, deque


class Person:

    def __init__(self, id, conn, x):
        self.id = id
        self.conn = conn
        self.x = x


def main():
    with open(0) as f:
        (N, M) = map(int, f.readline().split())
        info = [tuple(map(int, line.split())) for line in f.readlines()]
    people = [Person(i, conn=[], x=None) for i in range(N)]
    for (l, r, d) in info:
        people[l - 1].conn.append((r - 1, d))
        people[r - 1].conn.append((l - 1, -d))
    for person in people:
        if person.x is not None:
            continue
        else:
            person.x = person.id
            reserved = deque([person])
            seen = {person.id}
            while len(reserved) > 0:
                current = reserved.popleft()
                for (next_person_id, d) in current.conn:
                    if people[next_person_id].x is None:
                        people[next_person_id].x = current.x + d
                    elif people[next_person_id].x != current.x + d:
                        print('No')
                        return None
                    if next_person_id in seen:
                        continue
                    seen.add(next_person_id)
                    reserved.append(people[next_person_id])
    print('Yes')


main()
