__copyright__ = ''
__author__ = 'Son-Huy TRAN'
__email__ = 'sonhuytran@gmail.com'
__doc__ = ''
__version__ = '1.0'


def count_sessions(sessions: list) -> int:
    session_dict = {}
    for session in sessions:
        if session == 0:
            continue
        session_count = session_dict.get(session, 0)
        if session_count >= 2:
            return -1
        session_dict[session] = session_count + 1
    count = 0
    for value in session_dict.values():
        if value >= 2:
            count += 1
    return count


def main() -> int:
    n_calls = int(input())
    sessions = [int(word) for word in input().split()]
    print(count_sessions(sessions))
    return 0


def __starting_point():
    exit(main())


__starting_point()
