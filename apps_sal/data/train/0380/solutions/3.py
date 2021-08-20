class Solution:

    def isIPv4(self, IP):
        IP = IP.split('.')
        if len(IP) != 4:
            return False
        for ip in IP:
            if not ip.isdigit():
                return False
            if int(ip) > 255 or int(ip) < 0:
                return False
            if str(int(ip)) != ip:
                return False
        return True

    def isIPv6(self, IP):
        IP = IP.split(':')
        if len(IP) != 8:
            return False
        for ip in IP:
            ip = ip.lower()
            for c in ip:
                if (not c >= '0' or not c <= '9') and (not c >= 'a' or not c <= 'f'):
                    return False
            if len(ip) > 4 or len(ip) == 0:
                return False
            if int(ip, 16) > 65535 or int(ip, 16) < 0:
                return False
        return True

    def validIPAddress(self, IP):
        (f1, f2) = (0, 0)
        if ':' in IP:
            f1 = 1
        if '.' in IP:
            f2 = 1
        if f1 and f2:
            return 'Neither'
        if self.isIPv4(IP):
            return 'IPv4'
        elif self.isIPv6(IP):
            return 'IPv6'
        else:
            return 'Neither'
        '\n         :type IP: str\n         :rtype: str\n         '
