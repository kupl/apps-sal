FROM ubuntu:20.04

ARG USERNAME=apps
ARG DEBIAN_FRONTEND=noninteractive

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
        python3.9 \
        python3.9-dev \
        python3-pip \
        ssh-client \
        sudo && \
    apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*
RUN python3.9 -m pip install --no-cache-dir \
        autopep8 \
        pylint
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 309 && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.9 309

RUN useradd \
        --shell $(which bash) \
        -G sudo \
        -m -d /home/${USERNAME} -k /etc/skel \
        ${USERNAME} && \
    sed -i -e 's/%sudo.*/%sudo\tALL=(ALL:ALL)\tNOPASSWD:ALL/g' /etc/sudoers
