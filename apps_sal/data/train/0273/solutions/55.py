class Solution:
    def racecar(self, target: int) -> int:
        initial_state = (0, 1, 0)
        bfs = [initial_state]
        valid_actions = ['A', 'R']
        visited = set([(0, 1)])
        for position, speed, count in bfs:
            if position == target:
                return count

            for action in valid_actions:
                if action == 'A':
                    _position = position + speed
                    _speed = speed * 2

                elif action == 'R':
                    _position = position
                    if speed > 0:
                        _speed = -1
                    else:
                        _speed = 1

                if (_position, _speed) not in visited:
                    visited.add((_position, _speed))
                    bfs.append((_position, _speed, count + 1))

        return -1
